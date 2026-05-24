import React from "react";
import styled from "styled-components";
import QuestCard from "./QuestCard";

function QuestList({ quests, onUpdateQuest, onDeleteQuest }) {
  if (quests.length === 0) {
    return (
      <Empty>
        <EmptyIcon>🗺️</EmptyIcon>
        <p>No quests found. Create one to get started!</p>
      </Empty>
    );
  }

  return (
    <List>
      {quests.map((quest) => (
        <QuestCard
          key={quest.id}
          quest={quest}
          onUpdateQuest={onUpdateQuest}
          onDeleteQuest={onDeleteQuest}
        />
      ))}
    </List>
  );
}

const List = styled.div`
  display: flex;
  flex-direction: column;
  gap: 16px;
`;

const Empty = styled.div`
  text-align: center;
  padding: 48px;
  color: #888;
  font-size: 1.1rem;
`;

const EmptyIcon = styled.div`
  font-size: 3rem;
  margin-bottom: 12px;
`;

export default QuestList;