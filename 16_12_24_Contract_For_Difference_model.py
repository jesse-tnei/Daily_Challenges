purchase = {
    'market_share_price': 100,
    'broker_buy_price': 99.50,
    'broker_sell_price': 100.05,
    'order_fee_percentage': 0.01,
    'number_of_shares_traded': 2000
}

sale = {
    'market_share_price': 120,
    'broker_buy_price': 120.05,
    'broker_sell_price': 119.50,
    'order_fee_percentage': 0.01,
    'number_of_shares_traded': 1500

}
margin_call_percentage = 5


def cfd_purchase_cost():
    total_share_cost_buy_price = purchase['number_of_shares_traded'] * purchase['broker_sell_price']
    brokerage_fee = total_share_cost_buy_price * purchase['order_fee_percentage']
    margin_call_investment = total_share_cost_buy_price* margin_call_percentage
    total_purchase_cost = brokerage_fee+ margin_call_investment
    return total_purchase_cost


