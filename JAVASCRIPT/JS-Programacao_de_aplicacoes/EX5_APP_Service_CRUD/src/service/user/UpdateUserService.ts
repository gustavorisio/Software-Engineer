interface IUserRequest {
    id?: number;
    name: string;
    email: string;
    admin?: boolean;
    password: string;
}

class UpdateUserService {
    async execute({ name, email, admin = false, password }: IUserRequest) {
        if (!email) {
            throw new Error("Email Incorrect")
        }
        if (!name) {
            throw new Error("Name Incorrect")
        }
        return { message: "Registro incluido com sucesso" };
    }
}
export { UpdateUserService };