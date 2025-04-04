import { createTheme } from '@mui/material/styles';
import { ptBR } from '@mui/material/locale';
import { ptBR as DatePickersPtBR } from '@mui/x-date-pickers/locales';

import { colors } from './styles';

const theme = createTheme(
  {
    palette: {
      primary: {
        main: colors.primary,
        light: colors.primaryLight,
        dark: colors.primaryDark,
      },
      secondary: { main: colors.secondary },
      tertiary: { main: colors.tertiary },

      warning: { main: colors.warning },
      error: { main: colors.error },
      success: { main: colors.success },

      textInfo: { main: colors.textInfoColor },

      background: {
        default: colors.background,
        paper: colors.backgroundLighter,
      },

      backgroundStrokeActive: { dark: colors.backgroundStrokeActiveDark, main: colors.backgroundStrokeActive },
      backgroundElements: { dark: colors.backgroundElementsDarker, main: colors.backgroundElements, light: colors.backgroundElementsLighter },

      gray: { main: colors.gray },
      grayLight: { light: colors.grayLighter, main: colors.grayLight },      
    },
    typography: {
      fontFamily: 'Roboto, Trebuchet MS, Open Sans',
    },
  },
  ptBR,
  DatePickersPtBR
);

export default theme;
