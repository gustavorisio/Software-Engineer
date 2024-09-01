import { Request, Response } from "express";
class ListUsersController {
    async handle(request: Request, response: Response) {
        const users = [
        {
            name: "Gustavo",
            email: "gustavo@umc.com",
            admin: false,
            password: "1234",
        },
            {
                name:"UMC",
                email:"umc@umc.com",
                admin:false,
                password:"1234",
            }
    ];
        return response.json(users);
    }
}
export { ListUsersController };