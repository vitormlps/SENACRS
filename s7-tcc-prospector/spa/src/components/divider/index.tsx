import { FC } from 'react';

interface IDivider {
	vertical?: boolean;
}

const Divider: FC<IDivider> = ({ vertical }) => {
	const size = vertical ? { width: '1px' } : { height: '1px' };
	return (
		<hr
			style={{
				marginTop: '0',
				backgroundColor: '#d2d2d2',
				border: 'none',
				...size,
			}}
		/>
	);
};

export default Divider;
