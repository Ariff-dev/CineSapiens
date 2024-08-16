import { useState, useEffect } from 'react'

interface GetFetch {
  url: string
}

export function useGetFetch({ url }: GetFetch) {
  const [data, setData] = useState<any>(null)
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url)
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        const result = await response.json()
        setData(result)
        console.log(data)
      } catch (error) {
        setError(error instanceof Error ? error : new Error('Unknown error'))
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [url]) // Dependencia en `url`, para que se vuelva a ejecutar si `url` cambia

  return {
    data,
    loading,
    error,
  }
}
