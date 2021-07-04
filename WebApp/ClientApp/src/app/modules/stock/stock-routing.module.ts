import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StockDataComponent } from './components/stock-data/stock-data.component';
import { StockListComponent } from './components/stock-list/stock-list.component';

const routes: Routes = [
  {
    path: '',
    component: StockListComponent,
  },
  {
    path: 'data',
    component: StockDataComponent,
  },
];

@NgModule({
  imports: [[RouterModule.forChild(routes)]],
  exports: [RouterModule],
})
export class StockRoutingModule {}
