/** @odoo-module */
import {ListRenderer} from "@web/views/list/list_renderer";
import {MultiRecordSelector} from "@web/core/record_selectors/multi_record_selector";
import {useState} from "@odoo/owl";


export class FilterListRenderer extends ListRenderer {
    static template = "FilterListRenderer"

    setup() {
        super.setup();
        this.salesFilterState = useState({
            resIds: [],
            domain: [],
        })
    }

    get multiRecordProps() {
        return {
            placeholder: "Sales Person",
            resModel: "res.users",
            resIds: this.salesFilterState.resIds,
            domain: this.salesFilterState.domain,
            update: this.updateSPFilter.bind(this),
        }
    }

    updateSPFilter(userIds) {
        this.salesFilterState.resIds = userIds;
        this.salesFilterState.domain = userIds.length ? [["id", "not in", this.salesFilterState.resIds]] : [];
    }

    applySPFilter() {
        const {resIds} = this.salesFilterState
        const searchDomain = resIds.length ? [["user_id", "in", resIds]] : []
        this.env.searchModel.splitAndAddDomain(searchDomain)
    }
}

FilterListRenderer.components = {
    ...ListRenderer.components,
    MultiRecordSelector
}
