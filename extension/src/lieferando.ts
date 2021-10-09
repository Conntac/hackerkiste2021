// Lieferando values
interface product {
    productId: string,
    name: string,
    price: number,
    hasSizes: boolean,
    sizes: Array<size>
    product_info: meal_info
}

interface size {
    id: string,
    name: string,
    price: number
    sidedishgroups: Array<sidedishgroup>
}

interface sidedishgroup {
    sidedishes: Array<sidedish>
}

interface sidedish {
    id: string,
    name: string,
    price: number
}

// Parsed values
interface meal {
    id: string,
    name: string,
    description: string,
    price: number,
    meal_info: meal_info,
    side_meal_categories: Array<side_meal_category>
}

interface meal_info {
    text: string
}

interface side_meal_category {
    side_meals: Array<side_meal>
}

interface side_meal {
    id: string,
    name: string,
    description: string,
    price: number
}

declare var MenucardProducts: Array<product>

function fetch_products() {    
    if (!MenucardProducts || !Array.isArray(MenucardProducts)) {
        return []
    }

    let allergens = Array.from(document.querySelectorAll(".text-meal-allergens"))

    for (let idx = 0; idx < MenucardProducts.length; idx ++) {
        let product = MenucardProducts[idx]
        let product_html_element = document.getElementById(product.productId)
        let product_expand_button = product_html_element ? product_html_element.firstElementChild : undefined

        if (product_expand_button instanceof HTMLElement && product.hasSizes) {
            product_expand_button.click()
        }

        let allergen_button = allergens.find(function(element) {
            let attributes = element.attributes
            if (attributes) {
                let data_id = attributes.getNamedItem("data-id")
                if (data_id) {
                    return data_id.value == product.productId
                }
            }

            return false
        })

        if (allergen_button) {

        }
    }

    return parse_products(MenucardProducts)
}

function parse_products(products: Array<product>) {
    let meals: Array<meal> = []

    for (let product of products) {
        let side_meal_categories: Array<side_meal_category> = []
        let meal_info: meal_info = product.product_info

        if (Array.isArray(product.sizes) && product.sizes.length > 0) {
            let size = product.sizes[0]
            
            for (let sidedishgroup of size.sidedishgroups) {
                let side_meals: Array<side_meal> = []

                for (let sidedish of sidedishgroup.sidedishes) {
                    let side_meal: side_meal = {
                        id: sidedish.id,
                        name: sidedish.name,
                        description: "",
                        price: sidedish.price * 100
                    }

                    side_meals.push(side_meal)
                }

                let side_meal_category: side_meal_category = {
                    side_meals: side_meals
                }

                side_meal_categories.push(side_meal_category)
            }
        }

        let meal: meal = {
            id: product.productId,
            name: product.name,
            description: "",
            price: product.price * 100,
            meal_info: meal_info,
            side_meal_categories: side_meal_categories,
        }

        meals.push(meal)
    }

    return meals
}
