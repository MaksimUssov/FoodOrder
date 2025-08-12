<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import cardcomp from "./components/cardcomp.vue";

const dishes = ref("");
const workers = ref("");
const workerhistory = ref("");
const orderElement = ref("");
const cart = ref([]);
const createdOrderId = ref(null);
const idrand = ref(null);
const totalCost = ref(0);
const form = ref({
  date: "",
  worker_id: null,
});

onMounted(async () => {
  let response = await axios.get("api/dishes/");
  dishes.value = response.data;
  response = await axios.get("api/workers/");
  workers.value = response.data;
  response = await axios.get("api/dishoforder/");
  orderElement.value = response.data;
});

function addToCart(arr) {
  idrand.value = null;
  cart.value.push({
    id: arr[0],
    amount: arr[1],
    title: arr[2],
    cost: arr[3],
  });
}

function changePos(arr) {
  for (let index = 0; index < cart.value.length; index++) {
    if (cart.value[index].id == arr[0]) {
      cart.value[index].amount = arr[1];
      return;
    }
  }
}

function deletePos(idPos) {
  for (let index = 0; index < cart.value.length; index++) {
    if (cart.value[index].id == idPos) {
      cart.value.splice(index, 1);
    }
  }
}

function findTotalCost() {
  let totalCostFunc = 0;
  for (let index = 0; index < cart.value.length; index++) {
    totalCostFunc += cart.value[index].cost * cart.value[index].amount;
  }
  totalCost.value = totalCostFunc;
}

const submitForm = async () => {
  createdOrderId.value = null;
  const response = await axios.post("/api/order/", {
    date: form.value.date,
    worker_id: form.value.worker_id,
  });

  createdOrderId.value = response.data.id;

  for (let index = 0; index < cart.value.length; index++) {
    const response = await axios.post("/api/dishoforder/", {
      order_id: createdOrderId.value,
      dish_id: cart.value[index].id,
      dish_title: cart.value[index].title,
      worker_id: form.value.worker_id,
      date: form.value.date
    });
  }
  cart.value = "";
  findTotalCost();
};

function getRandomCart() {
  idrand.value = Math.floor(Math.random() * 32) + 33;
}
</script>
<template>
  <div class="menu__section">
    <div class="container">
      <div class="menu__title">
        <h1 id="pizza">ПИЦЦА</h1>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(0, 4)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(4, 8)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
    </div>
  </div>
  <div class="menu__section">
    <div class="container">
      <div class="menu__title">
        <h1 id="hot-dishes">ГОРЯЧИЕ БЛЮДА</h1>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(8, 12)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(12, 16)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
    </div>
  </div>
  <div class="menu__section">
    <div class="container">
      <div class="menu__title">
        <h1 id="soups">СУПЫ</h1>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(16, 20)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(20, 24)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
    </div>
  </div>
  <div class="menu__section">
    <div class="container">
      <div class="menu__title">
        <h1 id="drinks">НАПИТКИ</h1>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(24, 28)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
      <div class="row">
        <cardcomp
          v-for="dish in dishes.slice(28, 32)"
          :dish="dish"
          :key="dish.id"
          @addToCartEmit="addToCart"
          @changePosEmit="changePos"
          @deletePosEmit="deletePos"
          @findTotalCostEmit="findTotalCost"
        />
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="OrdersHistory"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="OrdersHistoryLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-scrollable">
      <div class="modal-content bg-dark text-light">
        <div
          class="modal-header"
          style="
            display: flex;
            align-items: center;
            justify-content: space-between;
          "
        >
          <h1 class="modal-title fs-5" id="OrdersHistoryLabel">
            История заказов
          </h1>
          <div style="display: flex; align-items: center; gap: 1rem">
            <form>
              <select
                name="worker"
                id="worker_id"
                class="form-select bg-dark text-light"
                v-model="workerhistory"
                required
              >
                <option :value="0" selected>Все</option>
                <option
                  v-for="worker in workers"
                  :key="worker.id"
                  :value="worker.id"
                >
                  {{ worker.name }}
                </option>
              </select>
            </form>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Закрыть"
              style="filter: invert(1)"
            ></button>
          </div>
        </div>
        <div class="modal-body">
          <table class="table table-dark">
            <thead>
              <tr>
                <th scope="col">Заказ</th>
                <th scope="col">Блюдо</th>
                <th scope="col">Дата</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(order, index) in orderElement" :key="index">
                <td v-if="order.worker_id == workerhistory">
                  {{ order.order_id }}
                </td>
                <td v-if="order.worker_id == workerhistory">
                  {{ order.dish_title }}
                </td>
                <td v-if="order.worker_id == workerhistory">
                  {{ order.date }}
                </td>
                <td v-if="workerhistory == 0">
                  {{ order.order_id }}
                </td>
                <td v-if="workerhistory == 0">
                  {{ order.dish_title }}
                </td>
                <td v-if="workerhistory == 0">
                  {{ order.date }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="ShopCart"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="ShopCartLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-scrollable">
      <div class="modal-content bg-dark text-light">
        <div
          class="modal-header"
          style="
            display: flex;
            align-items: center;
            justify-content: space-between;
          "
        >
          <h1 class="modal-title fs-5" id="ShopCartLabel">Корзина</h1>
          <div style="display: flex; align-items: center; gap: 1rem">
            <button
              type="button"
              class="btn"
              style="padding: 2px"
              @click="getRandomCart()"
            >
              <img
                src="../images/icons/cube-icon.png"
                style="width: 32px; height: 32px"
                alt=""
              />
              <span v-for="dish in dishes" :key="dish.id">
                <span v-if="dish.id == idrand">{{
                  (addToCart([idrand, 1, dish.title, dish.cost]),
                  findTotalCost())
                }}</span>
              </span>
            </button>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Закрыть"
              style="filter: invert(1)"
            ></button>
          </div>
        </div>
        <div class="modal-body">
          <table class="table table-dark">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Блюдо</th>
                <th scope="col">Количество</th>
                <th scope="col">Цена</th>
                <th scope="col">Сумма</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(pos, index) in cart">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ pos.title }}</td>
                <td>{{ pos.amount }}</td>
                <td>{{ pos.cost }}</td>
                <td>{{ pos.cost * pos.amount }}</td>
              </tr>
              <tr>
                <th colspan="4">Итог:</th>
                <th>{{ totalCost }} р.</th>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="modal-footer">
          <form
            @submit.prevent="submitForm"
            style="display: flex; flex-direction: column; row-gap: 1rem"
          >
            <input
              type="date"
              name="date"
              id="date"
              class="form-control bg-dark text-light"
              v-model="form.date"
              required
            />
            <select
              name="worker"
              id="worker_id"
              class="form-select bg-dark text-light"
              v-model="form.worker_id"
              required
            >
              <option :value="null" disabled>Сотрудник...</option>
              <option
                v-for="worker in workers"
                :key="worker.id"
                :value="worker.id"
              >
                {{ worker.name }}
              </option>
            </select>
            <button
              type="submit"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
              style="float: right"
            >
              Сделать заказ
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
