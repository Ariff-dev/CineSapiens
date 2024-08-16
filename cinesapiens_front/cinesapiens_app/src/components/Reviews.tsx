import { CardPost } from './Card'

export const Reviews = () => {
  return (
    <section className='flex flex-col gap-4'>
      <div>
        <h2 className='text-lg font-bold font-montserratAlternates'>
          Últimas reseñas
        </h2>
      </div>
      <div className='flex flex-col gap-4'>
        <CardPost />
        <CardPost />
      </div>
    </section>
  )
}
