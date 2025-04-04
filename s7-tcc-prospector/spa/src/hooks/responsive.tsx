import { FC, createContext, useContext } from 'react';
import { Theme, useMediaQuery } from '@mui/material';

import { IResponsiveContext } from '../types';

const ResponsiveContext = createContext<IResponsiveContext>({} as IResponsiveContext);

export const ResponsiveProvider: FC<any> = ({ children }) => {
	const xsUp = useMediaQuery((theme: Theme) => theme.breakpoints.up('xs')); // > 0px
	const smDown = useMediaQuery((theme: Theme) => theme.breakpoints.down('sm')); // < 600px
	const smUp = useMediaQuery((theme: Theme) => theme.breakpoints.up('sm')); // > 600px
	const mdDown = useMediaQuery((theme: Theme) => theme.breakpoints.down('md')); // < 900px
	const mdUp = useMediaQuery((theme: Theme) => theme.breakpoints.up('md')); // > 900px
	const lgDown = useMediaQuery((theme: Theme) => theme.breakpoints.down('lg')); // < 1200px
	const lgUp = useMediaQuery((theme: Theme) => theme.breakpoints.up('lg')); // > 1200px
	const xlDown = useMediaQuery((theme: Theme) => theme.breakpoints.down('xl')); // < 1536px
	const xlUp = useMediaQuery((theme: Theme) => theme.breakpoints.up('xl')); // > 1536px

	return (
		<ResponsiveContext.Provider
			value={{
				xsUp,
				smDown,
				smUp,
				mdDown,
				mdUp,
				lgDown,
				lgUp,
				xlDown,
				xlUp,
			}}
		>
			{children}
		</ResponsiveContext.Provider>
	);
};

export function useResponsive() {
	const context = useContext(ResponsiveContext);

	if (!context) {
		throw new Error('useResponsive must be used within an ResponsiveProvider');
	}

	return context;
}
