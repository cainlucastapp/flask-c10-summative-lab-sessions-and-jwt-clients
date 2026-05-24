import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import { Button } from "../styles";

function NavBar({ user, setUser }) {
  function handleLogoutClick() {
    fetch("/logout", { method: "DELETE" }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }

  return (
    <Wrapper>
      <Logo>
        <Link to="/">⚔️ Quest Tracker</Link>
      </Logo>
      <CharacterInfo>
        <ClassBadge>{user.character_class}</ClassBadge>
        <Stat>⚡ Level {user.level}</Stat>
        <Stat>💰 {user.gold} Gold</Stat>
        <Username>{user.username}</Username>
      </CharacterInfo>
      <Nav>
        <Button variant="outline" onClick={handleLogoutClick}>
          Logout
        </Button>
      </Nav>
    </Wrapper>
  );
}

const Wrapper = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
  background: #1a1a2e;
  color: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
`;

const Logo = styled.h1`
  font-family: "Permanent Marker", cursive;
  font-size: 1.8rem;
  color: gold;
  margin: 0;
  line-height: 1;

  a {
    color: inherit;
    text-decoration: none;
  }
`;

const CharacterInfo = styled.div`
  display: flex;
  align-items: center;
  gap: 16px;
`;

const ClassBadge = styled.span`
  background: indigo;
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
`;

const Stat = styled.span`
  color: #e0e0e0;
  font-size: 0.95rem;
  font-weight: 600;
`;

const Username = styled.span`
  color: gold;
  font-weight: bold;
  font-size: 1rem;
`;

const Nav = styled.nav`
  display: flex;
  gap: 8px;
  align-items: center;
`;

export default NavBar;
