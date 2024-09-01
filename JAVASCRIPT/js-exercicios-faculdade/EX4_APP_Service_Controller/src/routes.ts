import { Router } from "express";
import { CreateUserController } from "./controller/user/CreateUserController";
import { ListUsersController } from "./controller/user/ListUsersController";
import { UpdateUserController } from "./controller/user/UpdateUserController";

const router = Router();
const createUserController = new CreateUserController();
const listUsersController = new ListUsersController();
const updateUserController = new UpdateUserController();

router.post("/users", createUserController.handle);
router.get("/users", listUsersController.handle);
router.put("/users/:id", updateUserController.handle);

export {router};