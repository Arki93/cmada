import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import Account from '../views/dashboard/Account.vue'
/* import SignUp from '../views/SignUp.vue' */
import LogIn from '../views/LogIn.vue'
import Clients from '../views/dashboard/Clients.vue'
import Client from '../views/dashboard/Client.vue'
import AddClient from '../views/dashboard/AddClient.vue'
import UpdateClient from '../views/dashboard/UpdateClient.vue'
import UpdateTeam from '../views/dashboard/UpdateTeam.vue'
import Invoices from '../views/dashboard/Invoices.vue'
import Invoice from '../views/dashboard/Invoice.vue'
import NewInvoice from '../views/dashboard/NewInvoice.vue'
import Products from '../views/dashboard/Products.vue'
import AddProduct from '../views/dashboard/AddProduct.vue'
import Product from '../views/dashboard/Product.vue'
import UpdateProduct from '../views/dashboard/UpdateProduct.vue'

import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      title: 'CMada CRM | Acceuil'
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  /* {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp,
    meta: {
      title: 'CMada CRM | Création de Compte'
    }
  }, */
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn,
    meta: {
      title: 'CMada CRM | Connexion'
    }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Dashboard'
    }
  },
  {
    path: '/dashboard/clients',
    name: 'Clients',
    component: Clients,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Dashboard | Clients'
    }
  },
  {
    path: '/dashboard/clients/add',
    name: 'AddClient',
    component: AddClient,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Ajouter Client'
    }
  },
  {
    path: '/dashboard/client/:id',
    name: 'Client',
    component: Client,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Client Details'
    }
  },
  {
    path: '/dashboard/client/:id/update',
    name: 'UpdateClient',
    component: UpdateClient,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Modification Client'
    }
  },
  {
    path: '/dashboard/mon-compte',
    name: 'MonCompte',
    component: Account,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Mon Compte'
    }
  },
  {
    path: '/dashboard/mon-compte/update-team',
    name: 'UpdateTeam',
    component: UpdateTeam,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Modification Compte'
    }
  },
  {
    path: '/dashboard/factures',
    name: 'Factures',
    component: Invoices,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Factures'
    }
  },
  {
    path: '/dashboard/factures/:id',
    name: 'Facture',
    component: Invoice,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Détails Facture'
    }
  },
  {
    path: '/dashboard/factures/add',
    name: 'NewInvoice',
    component: NewInvoice,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Nouvelle Facture'
    }
  },
  {
    path: '/dashboard/products',
    name: 'Products',
    component: Products,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Produits'
    }
  },
  {
    path: '/dashboard/products/add',
    name: 'AddProduct',
    component: AddProduct,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Nouveau Produits'
    }
  },
  {
    path: '/dashboard/products/:id',
    name: 'Product',
    component: Product,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Détail Produit'
    }
  },
  {
    path: '/dashboard/products/:id/update-product',
    name: 'UpdateProduct',
    component: UpdateProduct,
    meta: {
      requireLogin: true,
      title: 'CMada CRM | Modifier Produit'
    }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  } else {
    document.title = 'CMada CRM'
  }

  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
