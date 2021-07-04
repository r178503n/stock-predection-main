import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    // component: IntelligenceComponent,
    loadChildren: () =>
      import('../stock/stock.module').then((mod) => mod.StockModule),
  },

  { path: '', redirectTo: '', pathMatch: 'full' },
];

@NgModule({
  imports: [[RouterModule.forChild(routes)]],
  exports: [RouterModule],
})
export class NavigationRoutingModule {}
