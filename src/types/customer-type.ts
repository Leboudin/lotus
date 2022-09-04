import { PlanDisplay } from "./plan-type";
import { SubscriptionType } from "./subscription-type";
export interface CustomerType {
  customer_name: string;
  billing_id?: string;
  balance?: string;
  customer_id: string;
}

export interface CustomerTableItem extends CustomerType {
  subscriptions: SubscriptionType[];
  total_revenue_due: number;
}

export interface CustomerSummary {
  customers: CustomerTableItem[];
}