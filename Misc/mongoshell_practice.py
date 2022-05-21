# db.purchase_orders.insertMany(
#     [
#         {product: "toothbrush", price: 4.75, customer: "Abhik"},
#         {product: "toothpaste", price: 199.99, customer: "Nishant"},
#         {product: "soap", price: 11.33, customer: "Shubham"},
#         {product: "handwash", price: 8.50, customer: "Sudha"},
#         {product: "toothpaste", price: 199.99, customer: "Abhik"},
#         {product: "soap", price: 11.33, customer: "Nishant"},
#         {product: "handwash", price: 8.50, customer: "Shubham"},
#         {product: "soap", price: 11.33, customer: "Sudha"}
#      ]
# )
#
# # How many toothbrush sold
#     db.purchase_orders.count({product: "toothbrush"})
#
# # List of all unique products
#     db.purchase_orders.distinct("product")
#
# # To find total amount of money spent by each customer
#     db.purchase_orders.aggregate(
#         [
#             {$match: {customer: {$in: ["Abhik"]}} },
#             {$group: {_id: "$customer", total: {$sum: "$price"}} }
#         ]
#     )
#
#
# # To find total amount of money spent on each product in descending order
#     db.purchase_orders.aggregate(
#         [
#             {$match: {} },
#             {$group: {_id: "$product", total: {$sum: "$price"}} },
#             {$sort: {total: -1}}
#         ]
#     )
#
# # Name in Alphabetical order
#     db.purchase_orders.aggregate(
#             [
#                 {$match: {} },
#                 {$group: {_id: "$customer", total: {$sum: "$price"}} },
#                 {$sort: {_id: 1}}
#             ]
#         )
#
#
