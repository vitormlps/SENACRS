import { createTheme } from '@mui/material';

const theme = createTheme(
    {
        palette:
        {
            primary: {
                main: '#987849'
            },
            text: {
                primary: '#000',
                secondary: '#010',
            },
            background: {
                default: '#EEEEEE',
                semiTransparent: '#00000055'
            },
            info: { main: '#FFFFFF' },
            cooling: '#2d8cf0',
            charging: '#59BA73',
            status: {
                online: '#19be6b',
                offline: '#6c6c6c',
                onSiteDebugging: '#e02020',
                remoteDebugging: '#ff9900',
                success: '#19be6b',
                warning: '#ff9900',
                error: '#e02020',
                unknown: '#6c6c6c'
            },
            error: { main: '#e70102' },
            cockpit: {
                background: '#232323',
                border: '#101010',
                resizableHandler: '#747474',
                onBackground: '#FFFFFF'
            },
            dividerOnDark: '#FFFFFF1F',
            tertiary: undefined,
            gray: undefined,
            grayLight: undefined,
            textInfo: undefined,
            backgroundStrokeActive: undefined,
            backgroundElements: undefined
        },
        typography: {
            appbar: {
                fontSize: '21pt',
                lineHeight: 1.6,
                fontWeight: 500,
                margin: 0,
            },
        },
        components: {
            MuiButton: {
                variants: [
                    {
                        props: { variant: 'mapBtn' },
                        style:
                        {
                            disableRipple: true,
                            fontWeight: 700,
                            color: '#987849',
                            backgroundColor: '#fafafa', 
                            '&:hover': 
                            {
                                color: '#fff',
                                backgroundColor: '#987849',
                            },
                            '&:disabled': 
                            {
                                color: '#dfdfdf',
                                backgroundColor: '#afafaf',
                                opacity: 0.9,
                            },
                        },
                    },
                    {
                        props: { variant: 'outlineFlightButton' },
                        style: (theme) =>
                        {
                            return {
                                border: `1px solid ${theme.theme.palette.primary.main}80`,
                                padding: '4px',
                                textTransform: 'none',
                                fontSize: '14px',
                                color: theme.theme.palette.primary.main,
                                '&:hover': 
                                {
                                    borderColor: theme.theme.palette.primary.main,
                                    backgroundColor: `${theme.theme.palette.primary.main}0a`
                                },
                                '&:disabled': 
                                {
                                    color: `${theme.theme.palette.primary.main}9c`,
                                    backgroundColor: '#e5e5e59c',
                                    border: '1px solid #cdcdcd9c'
                                },
                            };
                        }
                    },
                ],
            },
            MuiTypography:
            {
                styleOverrides:
                {
                    deviceButtonTitle: {
                        fontWeight: 'bold',
                        fontSize: '14px'
                    },
                    deviceButtonSubtitle: { fontSize: '12px' },
                    genericInfo: {
                        color: '#00000073',
                        letterSpacing: 0,
                        textAlign: 'center',
                        width: '100%',
                        fontSize: '12px',
                        lineHeight: '20px'
                    },
                    deviceDisplayItemTitle: {
                        color: '#00000073',
                        lineHeight: '20px',
                        fontSize: '14px',
                        textAlign: 'center',
                        width: '120px',
                        padding: '2px 5px 0'
                    },
                    deviceDisplayItemText: {
                        color: '#000000d9',
                        justifyContent: 'center',
                        alignItems: 'center',
                        height: '20px',
                        padding: '0 5px',
                        fontSize: '14px',
                        fontWeight: '550',
                    },
                    deviceStatusText: {
                        color: '#00000073',
                        letterSpacing: 0,
                        width: '100%',
                        fontSize: '14px',
                        lineHeight: '22px'
                    }
                },
                defaultProps:
                {
                    variantMapping:
                    {
                        appbar: 'h4',
                        deviceButtonTitle: 'span',
                        deviceButtonSubtitle: 'span',
                        genericInfo: 'span', 
                        deviceDisplayItemTitle: 'span',
                        deviceDisplayItemText: 'span'
                    },
                }
            },
            MuiDrawer: { defaultProps: { PaperProps: { sx: { backgroundColor: '#f0f0f0', } } } }
        },
    }
);

export default theme;