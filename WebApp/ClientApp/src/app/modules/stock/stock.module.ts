import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ApplicationSharedModules } from 'src/app/application-shared/modules/application-shared.module';
import { StockDataComponent } from './components/stock-data/stock-data.component';
import { StockListComponent } from './components/stock-list/stock-list.component';
import { StockRoutingModule } from './stock-routing.module';

@NgModule({
  imports: [CommonModule, StockRoutingModule, ApplicationSharedModules],
  declarations: [StockDataComponent, StockListComponent],
})
export class StockModule {}
