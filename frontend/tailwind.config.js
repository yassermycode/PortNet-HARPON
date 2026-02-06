/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f1f5',
          100: '#e1e3eb',
          200: '#c3c7d7',
          300: '#a5abc3',
          400: '#878faf',
          500: '#69739b',
          600: '#232a56',  // rgb(35, 42, 86) - Couleur principale
          700: '#1c2245',
          800: '#151934',
          900: '#0e1123',
          950: '#070912',
        },
        // Ajout de la couleur personnalisée directement accessible
        'custom-primary': 'rgb(35, 42, 86)',
      },
    },
  },
  plugins: [],
}
