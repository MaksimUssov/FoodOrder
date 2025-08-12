<script setup>
import { ref } from "vue";

const props = defineProps({
  dish: {
    type: Object,
    required: true,
    default: () => [],
  },
});

const emit = defineEmits([
    'addToCartEmit',
    'changePosEmit',
    'deletePosEmit',
    'findTotalCostEmit'
])

const count = ref(0);

function increment() {
  count.value++;
};

function decrement() {
  count.value--;
};

function add() {
    emit('addToCartEmit', [props.dish.id, count.value, props.dish.title, props.dish.cost])
    // console.log(props.dish.id)
}

function change() {
    emit('changePosEmit', [props.dish.id, count.value])
    // console.log(props.dish.id)
}

function del() {
    emit('deletePosEmit', props.dish.id)
    // console.log(props.dish.id)
}

function findTotalCost() {
    emit('findTotalCostEmit')
    // console.log(props.dish.id)
}

</script>
<template>
  <div class="col-md-3">
    <div class="card h-100" style="width: 19rem">
      <!-- <img src="images/food/lamb.jpg" class="card-img-top" alt="..." /> -->
      <div class="card-body">
        <h5 class="card-title">{{ dish.title }}</h5>
        <p class="card-text">
          {{ dish.composition }}
        </p>
      </div>
      <div class="card-footer text-center">
        <span class="cost">{{ dish.cost }}</span>
        <button type="button" class="add-to-cart btn btn-primary" v-if="count == 0" @click="increment(); add(); findTotalCost()">В корзину</button>
        <div class="add-to-cart" v-else>
            <button type="button" class="add-to-cart btn btn-primary" @click="decrement(); change(); findTotalCost()" v-if="count > 1">-</button>
            <button type="button" class="add-to-cart btn btn-primary" @click="decrement(); del(); findTotalCost()" v-else>-</button>
            <span>{{ count }}</span>
            <button type="button" class="add-to-cart btn btn-primary" @click="increment(); change(); findTotalCost()">+</button>
        </div>
      </div>
    </div>
  </div>
</template>
