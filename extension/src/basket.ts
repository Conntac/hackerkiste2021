import { resolveModuleName } from "../node_modules/typescript/lib/typescript";

export function inBasket(
    restaurantId: String,
    products: Array<any>,
): void {
    let prod_str = "";
    products.forEach((product: any) => {
        let prod_beg = `
        "id": "${product.id}",
        "productName": "${product.name}",
        "count": ${product.count},
        "basePrice": ${product.price},
        "basePricePickup": ${product.price},
        "deliveryType": 2,
        "ignoreMinimumOrderValue": false,
        `;

        let prod_mid = ""

        let basePrice = product.price * product.count;
        let totalPrice = product.price;
        let uniqueId = product.id;
        if(product.size && product.size != null) {
            let temp = ""
            product.size.forEach((dish: any) => {
                temp += `
                {
                    "id": "${dish.id}",
                    "sideDishName": "${dish.name}",
                    "price" : ${dish.price},
                    "pricePickup": ${dish.price},
                    "ignoreMinimumOrderValue": false
                },`;
                uniqueId += `-${dish.id}`;
                totalPrice += dish.price;
            });
            prod_mid = `
            "size": {
                "sideDishes": [
                    ${temp.substring(0, temp.length - 1)}
                ],
                "id": ${product.id},
                "sizeName": "${product.name}",
                "Price": "${product.price}",
                "PricePickup": ${product.price},
                "deliveryType": 2,
                "ignoreMinimumOrderValue": false
            },
            `;
        } else {
            prod_mid = `
            "size": null,
            `;
        }
        let prod_end = `
        "uniqueId": "${uniqueId}",
        "price": ${totalPrice},
        "pricePickup": ${totalPrice},
        "totalPriceMinimumOrder": ${totalPrice},
        "baseTotalPrice": ${basePrice},
        "baseTotalPricePickup": ${basePrice},
        "totalPrice": ${totalPrice * product.count},
        "totalPricePickup": ${totalPrice * product.count},
        "comment": null,
        "isDisabled": false
        `;
        prod_str += `
        {
            ${prod_beg}
            ${prod_mid}
            ${prod_end}
        },`;

    });
    let str = `
    {
        "${restaurantId}": {
           "products": [
                 ${prod_str.substring(0,prod_str.length - 1)}
           ],
           "voucher": null,
           "paymentMethod": null,
           "takeawayPay": [],
           "takeawayPayInitialized": false
        }
     }`;
    
    localStorage.setItem('basket', str);
    location.reload()

}