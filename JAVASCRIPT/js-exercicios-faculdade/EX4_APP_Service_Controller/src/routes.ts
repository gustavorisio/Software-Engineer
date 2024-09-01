import { Router } from "express";
import { CreateUserController } from "./controller/user/CreateUserController";
import { ListUsersController } from "./controller/user/ListUsersController";

const router = Router();
const createUserController = new CreateUserController();
const listUsersController = new ListUsersController();

router.post("/users", createUserController.handle);
router.get("/users", listUsersController.handle);

export {router};