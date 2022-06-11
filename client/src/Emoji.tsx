import React from 'react';
import { Emoji } from './client-axios';

export const EmojiComponent = ({ emoji, onClick}: { emoji?: Emoji, onClick: () => void}) =>{

  return (
    <div>
      <div style={{ fontSize: '100px', cursor: 'pointer'}} onClick={onClick}>
        {emoji?.text}
      </div>
      <div>rate: {emoji?.score}</div>
    </div>
  );
}