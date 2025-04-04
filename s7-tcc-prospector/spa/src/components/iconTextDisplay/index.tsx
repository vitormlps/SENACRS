import { FC } from 'react';
import { IIconTextDisplay } from '../../types';

const IconTextDisplay: FC<IIconTextDisplay> = (params: IIconTextDisplay) => {
	return (
		<div className='container flex center-y'>
			<div className='img-icon'>{params.icon}</div>
			<p className='my-0 mx-4'>{params.textContent}</p>
		</div>
	);
};

export default IconTextDisplay;
