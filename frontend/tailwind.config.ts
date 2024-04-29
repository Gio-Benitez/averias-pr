import forms from '@tailwindcss/forms';
import daisyui from 'daisyui';
import type { Config } from 'tailwindcss';
import typography from '@tailwindcss/typography';


/** @type {import('tailwindcss').Config}*/
const config = {
  content: [
    './src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        Inter: ['Inter', 'Satoshi', 'Alpino', 'sans-serif'],
        Satoshi: ['Satoshi', 'Inter', 'Alpino', 'sans-seri'],
        Alpino: ['Alpino', 'Inter', 'Satoshi', 'sans-seri']
      }
    }
  },
  daisyui: {
    themes: [
      'light',
      'dark',
      'dim',
      'cupcake',
      'retro',
      'business',
      'cyberpunk',
      'aqua',
      'valentine',
      'coffee',
      'forest',
      'night',
      'autumn',
      'corporate'
    ],
    styled: true,
    utils: true,
  },

  plugins: [forms, typography, daisyui]

} satisfies Config;

export default config;
