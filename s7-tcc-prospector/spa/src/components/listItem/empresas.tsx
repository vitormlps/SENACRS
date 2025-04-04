import { FC } from 'react';

import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { IListItems } from '../../types';
import { formatCnpj } from '../../utils/consts';
import { parseDateToString, parseStringDate } from '../../utils/dates';

const EmpresasListItem: FC<IListItems> = (params: IListItems) => {
	const getColumns = (item: any) => {
		const columns: GridColDef[] = [];
		const fields = Object.keys(item);

		for (let index = 0; index < fields.length; index++) {
			const header = fields[index];
			if (header.includes('_at') || header === 'id') continue;

			if (header === 'cnpj') {
				columns.push({
					field: header,
					headerName: header.toUpperCase(),
					width: 160,
					valueFormatter: (cell) => formatCnpj(cell.value),
				});
			} else if (header === 'capital_social') {
				columns.push({
					field: header,
					headerName: header.replaceAll('_', ' ').toUpperCase(),
					width: 130,
					valueFormatter: (cell) => `R$ ${cell.value},00`,
				});
			} else if (header === 'natureza_juridica') {
				columns.push({
					field: header,
					headerName: header.replaceAll('_', ' ').toUpperCase(),
					width: 190,
				});
			} else if (header === 'data_opcao_simples') {
				columns.push({
					field: header,
					headerName: 'Opção Simples',
					width: 130,
					valueFormatter: (cell) => {
						if (cell.value) {
							if (typeof cell.value === 'string') {
								return parseStringDate(cell.value);
							}
							return parseDateToString(cell.value);
						}
						return '-';
					},
				});
			} else {
				columns.push({
					field: header,
					headerName: header.replace('_id', '').replaceAll('_', ' ').toUpperCase(),
					width: 200,
				});
			}
		}
		return columns;
	};

	return (
		<div
			className='flex'
			style={{
				height: '89vh',
				minHeight: '40px',
				maxHeight: 'fit-content',
				backgroundColor: '#f8f8f8',
				border: `1px solid #f3f3f3`,
				borderRadius: '3px',
			}}
		>
			<DataGrid
				sx={{
					'& .MuiCheckbox-root': {
						color: '#c3c3c3',
					},
					'& .MuiCheckbox-root.Mui-checked': {
						color: 'secondary.main',
					},
				}}
				rows={params.items}
				columns={getColumns(params.items[0])}
				autoPageSize
				pagination
				checkboxSelection
				onSelectionModelChange={(ids) => {
					params.onSelect(ids);
				}}
			/>
		</div>
	);
};

export default EmpresasListItem;
