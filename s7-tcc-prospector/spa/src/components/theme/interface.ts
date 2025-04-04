import { createTheme } from '@mui/material/styles';

declare module '@mui/material/styles/createPalette' {
  interface Palette {
    tertiary: Palette['primary'];
    warningDark: Palette['primary'];
    gray: Palette['primary'];
    grayLight: Palette['primary'];
    textInfo: Palette['primary'];
    backgroundStrokeActive: Palette['primary'];
    backgroundElements: Palette['primary'];
  }
  interface PaletteOptions {
    tertiary: PaletteOptions['primary'];
    gray: PaletteOptions['primary'];
    grayLight: PaletteOptions['primary'];
    textInfo: PaletteOptions['primary'];
    backgroundStrokeActive: PaletteOptions['primary'];
    backgroundElements: PaletteOptions['primary'];
  }
}
