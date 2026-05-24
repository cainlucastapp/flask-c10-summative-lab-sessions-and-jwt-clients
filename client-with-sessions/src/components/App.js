import React, { useEffect, useState } from "react";
import NavBar from "./NavBar";
import Login from "../pages/Login";
import QuestBoard from "../pages/QuestBoard";

function App() {
  const [user, setUser] = useState(null);
  const [quests, setQuests] = useState([]);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);

  useEffect(() => {
    if (user) {
      fetch("/quests")
        .then((r) => r.json())
        .then((data) => setQuests(data.quests));
    }
  }, [user]);

  function handleAddQuest(newQuest) {
    setQuests((prev) => [newQuest, ...prev]);
  }

  function handleUpdateQuest(updatedQuest) {
    setQuests((prev) =>
      prev.map((q) => (q.id === updatedQuest.id ? updatedQuest : q))
    );
    if (updatedQuest.status === "completed") {
      setUser((prev) => ({
        ...prev,
        gold: prev.gold + updatedQuest.reward_gold,
      }));
    }
  }

  function handleDeleteQuest(id) {
    setQuests((prev) => prev.filter((q) => q.id !== id));
  }

  if (!user) return <Login onLogin={setUser} />;

  return (
    <>
      <NavBar user={user} setUser={setUser} />
      <main>
        <QuestBoard
          user={user}
          quests={quests}
          onAddQuest={handleAddQuest}
          onUpdateQuest={handleUpdateQuest}
          onDeleteQuest={handleDeleteQuest}
        />
      </main>
    </>
  );
}

export default App;