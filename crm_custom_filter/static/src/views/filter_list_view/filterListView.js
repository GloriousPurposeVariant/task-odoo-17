/** @odoo-module */
import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import {FilterListRenderer} from "./filterListRenderer";

export const filterListView = {
    ...listView,
    Renderer: FilterListRenderer
};

registry.category("views").add("filter_list_crm", filterListView);