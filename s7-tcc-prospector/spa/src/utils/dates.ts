export const parseStringDate = (date: string) => {
    const day = date.substring(8, 10)
    const month = date.substring(5, 7)
    const year = date.substring(0, 4)
    return `${day}/${month}/${year}`
};

export const parseDateToString = (date: Date) => {
    const day = date.getDate()
    const month = date.getMonth()
    const year = date.getFullYear()
    return `${day}/${month}/${year}`
};
