import React, { useState } from "react";
import styled from "styled-components";
import { Button, Error, Input, FormField, Label } from "../styles";

function NewQuestForm({ onAddQuest }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [difficulty, setDifficulty] = useState("");
  const [rewardGold, setRewardGold] = useState(0);
  const [errors, setErrors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  function handleSubmit(e) {
    e.preventDefault();
    setErrors([]);
    setIsLoading(true);

    fetch("/quests", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        description,
        difficulty,
        reward_gold: parseInt(rewardGold, 10),
      }),
    }).then((r) => {
      setIsLoading(false);
      if (r.ok) {
        r.json().then((quest) => {
          onAddQuest(quest);
          // Reset form
          setTitle("");
          setDescription("");
          setDifficulty("");
          setRewardGold(0);
        });
      } else {
        r.json().then((data) => setErrors(data.errors));
      }
    });
  }

  return (
    <FormWrapper>
      <FormTitle>⚔️ New Quest</FormTitle>
      <form onSubmit={handleSubmit}>
        <FormField>
          <Label htmlFor="title">Quest Title</Label>
          <Input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter quest title..."
          />
        </FormField>

        <FormField>
          <Label htmlFor="description">Description</Label>
          <StyledTextarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Describe the quest..."
            rows={3}
          />
        </FormField>

        <FormRow>
          <FormField>
            <Label htmlFor="difficulty">Difficulty</Label>
            <StyledSelect
              id="difficulty"
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value)}
            >
              <option value="">Select difficulty...</option>
              <option value="Easy">Easy</option>
              <option value="Medium">Medium</option>
              <option value="Hard">Hard</option>
              <option value="Legendary">Legendary</option>
            </StyledSelect>
          </FormField>

          <FormField>
            <Label htmlFor="reward_gold">Gold Reward</Label>
            <Input
              type="number"
              id="reward_gold"
              value={rewardGold}
              min="0"
              max="100000"
              onChange={(e) => setRewardGold(e.target.value)}
            />
          </FormField>
        </FormRow>

        <FormField>
          {errors.map((err) => (
            <Error key={err}>{err}</Error>
          ))}
        </FormField>

        <FormField>
          <Button variant="fill" color="primary" type="submit">
            {isLoading ? "Creating..." : "Create Quest"}
          </Button>
        </FormField>
      </form>
    </FormWrapper>
  );
}

const FormWrapper = styled.div`
  background: white;
  border-radius: 10px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  border-left: 5px solid indigo;
`;

const FormTitle = styled.h3`
  margin: 0 0 20px;
  color: #1a1a2e;
  font-size: 1.2rem;
`;

const FormRow = styled.div`
  display: flex;
  gap: 16px;

  & > div {
    flex: 1;
  }
`;

const StyledTextarea = styled.textarea`
  border-radius: 6px;
  border: 1px solid #dbdbdb;
  width: 100%;
  font-size: 1rem;
  line-height: 1.5;
  padding: 4px;
  resize: vertical;
  font-family: inherit;
`;

const StyledSelect = styled.select`
  width: 100%;
  padding: 4px;
  font-size: 1rem;
  border-radius: 6px;
  border: 1px solid #dbdbdb;
`;

export default NewQuestForm;