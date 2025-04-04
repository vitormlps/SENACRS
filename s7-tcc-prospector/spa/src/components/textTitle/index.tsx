import { FC } from 'react';

interface ITitle {
	title: string;
}

const Title: FC<ITitle> = ({ title }) => {
	return <h3 className='flex center bold text primary m-0'>{title}</h3>;
};

export default Title;
