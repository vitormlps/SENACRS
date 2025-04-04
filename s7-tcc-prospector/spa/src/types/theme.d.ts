import * as mui from '@mui/material';

declare module '@mui/material' {
    export default mui;
    export interface ButtonPropsVariantOverrides {
        mapBtn: true;
        outlineFlightButton: true;
    }
}

declare module '@mui/material/styles' {
    interface TypographyVariants {
        appbar: React.CSSProperties;
        deviceButtonTitle: React.CSSProperties;
        deviceButtonSubtitle: React.CSSProperties;
    }
  
    interface TypographyVariantsOptions {
        appbar?: React.CSSProperties;
        deviceButtonTitle?: React.CSSProperties;
        deviceButtonSubtitle?: React.CSSProperties;
    }

}
  
declare module '@mui/material/Typography' {
    interface TypographyPropsVariantOverrides {
        appbar: true;
        deviceButtonTitle: true;
        deviceButtonSubtitle: true;
        genericInfo: true;
        deviceDisplayItemTitle: true;
        deviceDisplayItemText: true;
        deviceStatusText: true;
    }

    interface TypographyClasses {
        deviceButtonTitle: true;
        deviceButtonSubtitle: true;
        genericInfo: true;
        deviceDisplayItemTitle: true;
        deviceDisplayItemText: true;
        deviceStatusText: true;
    }
}

declare module '@mui/material/styles/createPalette'
{
    interface TypeBackground
    {
        semiTransparent: string;
    }

    interface PaletteOptions {
        cooling?: string;
        charging?: string;
        status?: {
            online: string;
            offline: string;
            onSiteDebugging: string;
            remoteDebugging: string;
            success: string;
            warning: string;
            error: string;
            unknown: string;
        };
        cockpit: {
            background: string;
            border: string;
            resizableHandler: string;
            onBackground: string;
        };
        dividerOnDark: string;
    }

    interface Palette {
        cooling?: string;
        charging?: string;
        status?: {
            online: string;
            offline: string;
            onSiteDebugging: string;
            remoteDebugging: string;
            success: string;
            warning: string;
            error: string;
            unknown: string;
        };
        cockpit: {
            background: string;
            border: string;
            resizableHandler: string;
            onBackground: string;
        };
        dividerOnDark: string;
    }
}