import React, { useState } from "react";
import styled from "styled-components";
import QuestList from "../components/QuestList";
import NewQuestForm from "../components/NewQuestForm";
import { Button } from "../styles";

function QuestBoard({ user, quests, onAddQuest, onUpdateQuest, onDeleteQuest }) {
  const [showForm, setShowForm] = useState(false);
  const [sortBy, setSortBy] = useState("date");
  const [filterBy, setFilterBy] = useState("all");

  function getSortedAndFilteredQuests() {
    let filtered = [...quests];

    // Filter
    if (filterBy !== "all") {
      filtered = filtered.filter((q) => q.status === filterBy);
    }

    // Sort
    switch (sortBy) {
      case "difficulty":
        const difficultyOrder = { Easy: 1, Medium: 2, Hard: 3, Legendary: 4 };
        filtered.sort((a, b) => difficultyOrder[b.difficulty] - difficultyOrder[a.difficulty]);
        break;
      case "gold":
        filtered.sort((a, b) => b.reward_gold - a.reward_gold);
        break;
      case "status":
        const statusOrder = { active: 1, completed: 2, failed: 3 };
        filtered.sort((a, b) => statusOrder[a.status] - statusOrder[b.status]);
        break;
      case "date":
      default:
        filtered.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
        break;
    }

    return filtered;
  }

  const activeCount = quests.filter((q) => q.status === "active").length;
  const completedCount = quests.filter((q) => q.status === "completed").length;
  const failedCount = quests.filter((q) => q.status === "failed").length;

  return (
    <Wrapper>
      <Header>
        <Title>📜 Quest Board</Title>
        <Button variant="fill" color="primary" onClick={() => setShowForm((prev) => !prev)}>
          {showForm ? "Cancel" : "+ New Quest"}
        </Button>
      </Header>

      {showForm && (
        <NewQuestForm
          onAddQuest={(quest) => {
            onAddQuest(quest);
            setShowForm(false);
          }}
        />
      )}

      <StatsRow>
        <StatCard>
          <StatNumber>{quests.length}</StatNumber>
          <StatLabel>Total Quests</StatLabel>
        </StatCard>
        <StatCard color="green">
          <StatNumber>{activeCount}</StatNumber>
          <StatLabel>Active</StatLabel>
        </StatCard>
        <StatCard color="gold">
          <StatNumber>{completedCount}</StatNumber>
          <StatLabel>Completed</StatLabel>
        </StatCard>
        <StatCard color="red">
          <StatNumber>{failedCount}</StatNumber>
          <StatLabel>Failed</StatLabel>
        </StatCard>
      </StatsRow>

      <Controls>
        <ControlGroup>
          <label>Filter:</label>
          <select value={filterBy} onChange={(e) => setFilterBy(e.target.value)}>
            <option value="all">All</option>
            <option value="active">Active</option>
            <option value="completed">Completed</option>
            <option value="failed">Failed</option>
          </select>
        </ControlGroup>
        <ControlGroup>
          <label>Sort by:</label>
          <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
            <option value="date">Date</option>
            <option value="difficulty">Difficulty</option>
            <option value="gold">Gold Reward</option>
            <option value="status">Status</option>
          </select>
        </ControlGroup>
      </Controls>

      <QuestList
        quests={getSortedAndFilteredQuests()}
        onUpdateQuest={onUpdateQuest}
        onDeleteQuest={onDeleteQuest}
      />
    </Wrapper>
  );
}

const Wrapper = styled.div`
  max-width: 900px;
  margin: 32px auto;
  padding: 0 16px;
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
`;

const Title = styled.h2`
  font-size: 1.8rem;
  margin: 0;
  color: #1a1a2e;
`;

const StatsRow = styled.div`
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
`;

const StatCard = styled.div`
  flex: 1;
  background: ${(p) =>
    p.color === "green" ? "#e8f5e9" :
    p.color === "gold" ? "#fff8e1" :
    p.color === "red" ? "#ffebee" : "#f5f5f5"};
  border-radius: 8px;
  padding: 16px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.08);
`;

const StatNumber = styled.div`
  font-size: 2rem;
  font-weight: bold;
  color: #1a1a2e;
`;

const StatLabel = styled.div`
  font-size: 0.85rem;
  color: #666;
  margin-top: 4px;
`;

const Controls = styled.div`
  display: flex;
  gap: 24px;
  margin-bottom: 24px;
  align-items: center;
`;

const ControlGroup = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;

  label {
    font-weight: 600;
    color: #444;
  }

  select {
    padding: 6px 10px;
    border-radius: 6px;
    border: 1px solid #dbdbdb;
    font-size: 0.95rem;
  }
`;

export default QuestBoard;