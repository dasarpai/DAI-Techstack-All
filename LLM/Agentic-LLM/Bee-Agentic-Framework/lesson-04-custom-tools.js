import {z} from "zod";
import {DynamicTool, StringToolOutput} from "bee-agent-framework/tools/base";

export const createSupportTicket = new DynamicTool({
    name: "CreateSupportTicket",
    description:"Create a support ticket",
    inputSchema : z.object({
        description:z.string(),
    }),
    async handler(input){
        const tiketNumber = Math.floor(Math.random()*100000)
        return new StringToolOutput(`Ticket #${tiketNumber} created successfully`);

    }
});