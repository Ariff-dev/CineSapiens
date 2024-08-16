interface CardPost {
  image_url?: string
  post_title?: string
  post_description?: string
}

export const CardPost = ({
  image_url,
  post_description,
  post_title,
}: CardPost) => {
  return (
    <div className='bg-[url(https://m.media-amazon.com/images/I/81Rrx-Bv+6L._AC_UF894,1000_QL80_.jpg)] bg-cover rounded-md'>
      <div className=' bg-black/50 w-full h-[500px] flex flex-col  justify-end mx rounded-md'>
        <div className='p-4'>
          <p className='text-2xl font-bold'>Dune</p>
          <p>
            En un lejano futuro, la galaxia conocida es gobernada mediante un
            ...
          </p>
        </div>
      </div>
    </div>
  )
}
