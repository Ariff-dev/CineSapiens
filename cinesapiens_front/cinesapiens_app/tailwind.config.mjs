/** @type {import('tailwindcss').Config} */

export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'color-bg-1': '#2E2C2F',
        'color-bg-2': '#0F0F0F',
        'color-component-1': '#05A577',
        'color-component-2': '#383838',
        'color-component-3': '#303030',
        'color-component-nav1': '#007352',
        'color-component-nav-2': '#05A577',
        'text-color-cp': '#06E0A2',
        'text-anchord': '#0EB1D2',
      },
      fontFamily: {
        montserrat: ['montserrat', 'serif'],
        montserratAlternates: ['Montserrat Alternates', 'serif'],
      },
    },
  },
  plugins: [],
}
