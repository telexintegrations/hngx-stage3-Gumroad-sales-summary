import requests


def getGumroadData(gumroadAPIKey: str, returnURL: str):
    try:
        gumroadSalesAPIUrl = f"https://api.gumroad.com/v2/sales?access_token={gumroadAPIKey}"
        salesResponse = requests.get(gumroadSalesAPIUrl)

        gumroadUserAPIUrl = f"https://api.gumroad.com/v2/user?access_token={gumroadAPIKey}"
        usernameResponse = requests.get(gumroadUserAPIUrl)

        if salesResponse.status_code != "200" or usernameResponse.status_code != "200":
            error_payload = {
                "message": "Invalid Request",
                "username": "Gumroad Revenue Tracker",
                "event_name": "Sales Summary",
                "status": "error"
            }

            requests.post(returnURL, json=error_payload)
            return

        gumroadSalesData = salesResponse.json()
        gumroadUsernameData = usernameResponse.json()

        formattedReport = salesReport(gumroadSalesData, gumroadUsernameData)

        responsePayload = {
            "message": formattedReport,
            "username": "Gumroad Revenue Tracker",
            "event_name": "Sales Summary",
            "status": "success"
        }

        requests.post(returnURL, json=responsePayload)

    except Exception as e:
        error_payload = {"error": str(e)}
        requests.post(returnURL, json=error_payload)


def salesReport(gumroadSalesData, gumroadUsernameData):
    if not gumroadUsernameData.get("success"):
        return "The User does not exist."

    if not gumroadSalesData.get("success"):
        return "No sales data available"

    sales = gumroadSalesData.get("sales", [])

    if not sales:
        f"Hello, {gumroadUsernameData['user']['name']} \nYou have no recent sales record"

    totalRevenue = sum(float(sale.get("formatted_total_price","$0").replace("$", "")) for sale in sales)
    total_sales = len(sales)

    report = (
        f"📊 **Gumroad Sales Summary** 📊\n"
        f"🛒 Total Sales: **{total_sales}**\n"
        f"💰 Total Revenue: **${totalRevenue:.2f}**\n\n"
        f"📦 **Recent Transactions:**\n"
    )

    for sale in sales[:5]:
        product_name = sale.get("product_name", "Unknown Product")
        price = sale.get("formatted_total_price", "N/A")
        timestamp = sale.get("created_at", "Unknown Date")

        report += f"• 🏷️ **{product_name}** - {price} ({timestamp})\n"

    return report
