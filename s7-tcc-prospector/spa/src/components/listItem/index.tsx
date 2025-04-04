import { FC } from 'react';

import { theme } from '..';
import { Tooltip, Checkbox } from '@mui/material';
import { IListItem } from '../../types';

const ListItem: FC<IListItem> = (params: IListItem) => {
	return (
		<div
			className='flex'
			style={{
				paddingRight: '5%',
				marginBottom: '1.5%',
				backgroundColor: '#fafafa',
				border: `1px solid ${theme.palette.backgroundElements.main}`,
				borderRadius: '3px',
				minHeight: '32px',
				maxHeight: 'fit-content',
			}}
		>
			<Checkbox
				size='small'
				checked={
					params.selectedItemsIds.find((itemId) => itemId === params.item.id) !==
					undefined
				}
				onClick={() => params.onSelect(params.item.id)}
			/>

			<div className='flex px-1'>
				<span className='flex center text-10 nowrap m-0'>{params.item.id}</span>
			</div>

			<Tooltip
				title={params.item.descricao}
				placement='right'
				disableFocusListener
				disableTouchListener
				followCursor
			>
				<div className='flex of-hidden px-1'>
					<span className='flex center text-11 nowrap m-0'>{params.item.descricao}</span>
				</div>
			</Tooltip>
		</div>
	);
};

export default ListItem;
