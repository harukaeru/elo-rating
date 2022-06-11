import React from 'react';
import { useEmojis } from './hooks'
import { EmojiComponent } from './Emoji'

export function App() {

  const { emojis, decideOneEmoji } = useEmojis()

  return (
    <div className="App">
      <header className="App-header">
        <div>Battle</div>
        <div>
          <EmojiComponent emoji={emojis.left} onClick={() => {
            decideOneEmoji(emojis.left, emojis.right, emojis.left)
          }} />
          <EmojiComponent emoji={emojis.right} onClick={() => {
            decideOneEmoji(emojis.left, emojis.right, emojis.right)
          }} />
        </div>
      </header>
    </div>
  );
}