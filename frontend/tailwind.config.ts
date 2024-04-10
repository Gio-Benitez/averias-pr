import forms from '@tailwindcss/forms';
import daisyui from 'daisyui';
import type { Config } from 'tailwindcss';
import { skeleton } from '@skeletonlabs/tw-plugin';

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
      {
        dark: {
          primary: '#ff3e00',
          secondary: '#3b82f6',
          accent: '#fde047',
          neutral: '#ffffff',
          'base-100': '#001820',
          info: '#2dd4bf',
          success: '#4ade80',
          warning: '#fbbd23',
          error: '#fb7185'
        },
        light: {
          primary: '#ff3e00',
          secondary: '#3b82f6',
          accent: '#fde047',
          neutral: '#001820',
          'base-100': '#ffffff',
          info: '#2dd4bf',
          success: '#4ade80',
          warning: '#fbbd23',
          error: '#fb7185'
        }
      },
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
    ]
  },
  plugins: [forms, skeleton, daisyui]
} satisfies Config;

export default config;
