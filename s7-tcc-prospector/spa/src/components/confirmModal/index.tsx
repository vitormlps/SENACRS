import { FC } from 'react';
import { Box, Button, Grid, Modal, Typography } from '@mui/material';
import { IConfirmModal } from '../../types';

const style = {
	position: 'absolute' as 'absolute',
	top: '50%',
	left: '50%',
	transform: 'translate(-50%, -50%)',
	width: 400,
	bgcolor: 'background.paper',
	border: '2px solid #000',
	boxShadow: 24,
	p: 4,
};

const ReportConfirmModal: FC<IConfirmModal> = (props: IConfirmModal) => {
	return (
		<Modal open={props.open} onClose={props.onClose}>
			<Box sx={style}>
				<Box display='flex' flexDirection='column' alignItems='center'>
					<Typography fontSize={24} textAlign='center'>
						Deseja exportar o relatório com ou sem imagens?
					</Typography>

					<Grid container columnSpacing='24px' paddingTop='24px'>
						<Grid item xs={6}>
							<Button
								variant='contained'
								color='secondary'
								fullWidth
								onClick={() => props.onConfirm(true)}
							>
								<Typography
									color='white'
									fontSize='14px'
									fontWeight='700'
									lineHeight='24px'
									letterSpacing='0.5px'
									textTransform='initial'
								>
									Com imagens
								</Typography>
							</Button>
						</Grid>
						<Grid item xs={6}>
							<Button
								variant='contained'
								color='secondary'
								fullWidth
								onClick={() => props.onConfirm(false)}
							>
								<Typography
									color='white'
									fontSize='14px'
									fontWeight='700'
									lineHeight='24px'
									letterSpacing='0.5px'
									textTransform='initial'
								>
									Sem imagens
								</Typography>
							</Button>
						</Grid>
					</Grid>
				</Box>
			</Box>
		</Modal>
	);
};

export default ReportConfirmModal;
