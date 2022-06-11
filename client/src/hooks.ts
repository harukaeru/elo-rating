import React, { useEffect } from "react"
import { Emoji, EmojisApi } from "./client-axios"

export const useEmojis = () => {
  const [emojis, setEmojis] = React.useState({
    left: {
      id: 0,
      text: '',
      score: '0',
    },
    right: {
      id: 0,
      text: '',
      score: '0',
    }
  })

  const requestNewEmojis = () => {
    new EmojisApi().listEmojis()
    .then(res => res.data)
    .then(emojis => 
      setEmojis({
        left: {
          id: emojis[0].id,
          text: emojis[0].text ? emojis[0].text : '',
          score: emojis[0].score ? emojis[0].score : '0',
        },
        right: {
          id: emojis[1].id,
          text: emojis[1].text ? emojis[1].text : '',
          score: emojis[1].score ? emojis[1].score : '0',
        },
      }))
  }

  const decideOneEmoji = (leftEmoji: Emoji, rightEmoji: Emoji, decidedEmoji: Emoji) => {
    const doubleEmoji = {
      left: leftEmoji,
      right: rightEmoji,
      decided: decidedEmoji,
    }
    new EmojisApi().decideOneEmoji(doubleEmoji).then(requestNewEmojis)
  }

  useEffect(requestNewEmojis, [])

  return {emojis, decideOneEmoji}
}


