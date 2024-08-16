// OpinionsPost.tsx
import React from 'react'
import { OpinionCard } from './OpinionCard'
import { useGetFetch } from '../hooks/useGetFetch'

const OpinionsPost: React.FC = () => {
  const { data, loading, error } = useGetFetch({
    url: 'http://localhost:5000/get_posts',
  })

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <div className='flex flex-col gap-6'>
      <h4 className='text-xl font-bold font-montserratAlternates'>
        Opiniones destacadas
      </h4>
      {Array.isArray(data) && data.length > 0 ? (
        data.map((post: any) => (
          <OpinionCard key={post.id_post_sa} post={post} />
        ))
      ) : (
        <div>No posts available</div>
      )}
    </div>
  )
}

export default OpinionsPost
