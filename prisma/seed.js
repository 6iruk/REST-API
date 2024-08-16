const { PrismaClient } = require('@prisma/client')

const prisma = new PrismaClient()

const userData = [
  {
    email: 'dani@suresupplies.com',
    supplier: {
      create: 
        {
          name: 'Daniel',
          phone: '+251 921 586-325',
        },
    },
  },
  {
    driver: {
      create: 
        {
          name: 'Asmamaw',
          phone: '+251 922 592-372',
        },
    },
  },
  {
    email: 'gizachew@suresupplies.com',
    supplier: {
      create: 
        {
          name: 'Gizachew',
          phone: '+251 911 428-340',
        },
    },
  },
]

const productData = [
      {
        name: 'Sand',
        price: 500.00,
        description: 'High quality sand from the low-lands of ethiopia.',
        supplierId: 1,
      },
      {
        name: 'Cement',
        price: 800.00,
        description: 'Local cement.',
        supplierId: 2,
      },
]

const orderData = [
    {
      productId: null,
      driverId: 1,
      deliveryAddress: 'Addis Ababa, yeka W03',
      quantity: 2,
      price: 1600.00,
    },
]
async function main() {
  console.log(`Start seeding ...`)
  var user = await prisma.user.create({
    data: userData[0],
  })

  user = await prisma.user.create({
    data: userData[1],
  })


  user = await prisma.user.create({
    data: userData[2],
  })


  var product = await prisma.product.create({
    data: productData[0],
  })

  orderData[0].productId = product.id;

  product = await prisma.product.create({
    data: productData[1],
  })

  product = await prisma.order.create({
    data: orderData[0],
  })

  console.log(`Seeding finished.`)
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })
