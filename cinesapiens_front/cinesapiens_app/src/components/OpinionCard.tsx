import React from 'react'

export const OpinionCard = ({ post }: any) => {
  return (
    <div className='card'>
      <h5>{post.post_name}</h5>
      <p>{post.post_description}</p>
    </div>
  )
}
