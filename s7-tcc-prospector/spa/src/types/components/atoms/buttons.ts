interface IEmpresasButton {
    service: any;
    selectedIds: string[];
    exportingFile: boolean;
}

interface IImageUri {
    images: string;
  }

interface IConfirmDetectionAction {
}

export type {
    IEmpresasButton,
    IImageUri,
    IConfirmDetectionAction,
};