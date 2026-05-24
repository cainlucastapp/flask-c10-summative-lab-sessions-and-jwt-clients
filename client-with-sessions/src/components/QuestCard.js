import React, { useState } from "react";
import styled from "styled-components";
import { Button } from "../styles";

const DIFFICULTY_COLORS = {
  Easy: "#4caf50",
  Medium: "#ff9800",
  Hard: "#f44336",
  Legendary: "#9c27b0",
};

const STATUS_COLORS = {
  active: "#2196f3",
  completed: "#4caf50",
  failed: "#f44336",
};

function QuestCard({ quest, onUpdateQuest, onDeleteQuest }) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const isLocked = quest.status === "completed" || quest.status === "failed";

  function handleStatusUpdate(newStatus) {
    setIsLoading(true);
    setError(null);
    fetch(`/quests/${quest.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status: newStatus }),
    })
      .then((r) => r.json())
      .then((data) => {
        setIsLoading(false);
        if (data.errors) {
          setError(data.errors[0]);
        } else {
          onUpdateQuest(data);
        }
      });
  }

  function handleDelete() {
    setIsLoading(true);
    fetch(`/quests/${quest.id}`, { method: "DELETE" }).then((r) => {
      setIsLoading(false);
      if (r.ok) {
        onDeleteQuest(quest.id);
      }
    });
  }

  return (
    <Card locked={isLocked}>
      <CardHeader>
        <TitleRow>
          <QuestTitle>{quest.title}</QuestTitle>
          <Badges>
            <DifficultyBadge color={DIFFICULTY_COLORS[quest.difficulty]}>
              {quest.difficulty}
            </DifficultyBadge>
            <StatusBadge color={STATUS_COLORS[quest.status]}>
              {quest.status.charAt(0).toUpperCase() + quest.status.slice(1)}
            </StatusBadge>
          </Badges>
        </TitleRow>
        <GoldReward>💰 {quest.reward_gold} Gold</GoldReward>
      </CardHeader>

      <Description>{quest.description}</Description>

      {error && <ErrorText>{error}</ErrorText>}

      {isLocked ? (
        <LockedMessage>
          {quest.status === "completed" ? "✅ Quest Complete" : "❌ Quest Failed"} — Locked
        </LockedMessage>
      ) : (
        <Actions>
          <Button
            variant="fill"
            color="primary"
            onClick={() => handleStatusUpdate("completed")}
            disabled={isLoading}
          >
            ✅ Complete
          </Button>
          <Button
            variant="outline"
            color="primary"
            onClick={() => handleStatusUpdate("failed")}
            disabled={isLoading}
          >
            ❌ Fail
          </Button>
          <Button
            variant="outline"
            color="secondary"
            onClick={handleDelete}
            disabled={isLoading}
          >
            🗑️ Delete
          </Button>
        </Actions>
      )}

      {isLocked && (
        <DeleteRow>
          <Button
            variant="outline"
            color="secondary"
            onClick={handleDelete}
            disabled={isLoading}
          >
            🗑️ Delete
          </Button>
        </DeleteRow>
      )}

      <DateText>
        Created: {new Date(quest.created_at).toLocaleDateString()}
      </DateText>
    </Card>
  );
}

const Card = styled.div`
  background: ${(p) => (p.locked ? "#f9f9f9" : "white")};
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  border-left: 5px solid ${(p) => (p.locked ? "#ccc" : "indigo")};
  opacity: ${(p) => (p.locked ? 0.8 : 1)};
`;

const CardHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
`;

const TitleRow = styled.div`
  display: flex;
  flex-direction: column;
  gap: 6px;
`;

const QuestTitle = styled.h3`
  margin: 0;
  font-size: 1.1rem;
  color: #1a1a2e;
`;

const Badges = styled.div`
  display: flex;
  gap: 8px;
`;

const DifficultyBadge = styled.span`
  background: ${(p) => p.color};
  color: white;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: bold;
`;

const StatusBadge = styled.span`
  background: ${(p) => p.color};
  color: white;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: bold;
`;

const GoldReward = styled.span`
  font-weight: bold;
  color: #b8860b;
  font-size: 0.95rem;
  white-space: nowrap;
`;

const Description = styled.p`
  color: #555;
  font-size: 0.95rem;
  margin: 8px 0 16px;
  line-height: 1.5;
`;

const Actions = styled.div`
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
`;

const LockedMessage = styled.div`
  color: #888;
  font-style: italic;
  font-size: 0.9rem;
  margin-bottom: 8px;
`;

const DeleteRow = styled.div`
  margin-top: 8px;
`;

const ErrorText = styled.p`
  color: red;
  font-size: 0.85rem;
  margin-bottom: 8px;
`;

const DateText = styled.p`
  color: #aaa;
  font-size: 0.8rem;
  margin: 12px 0 0;
`;

export default QuestCard;