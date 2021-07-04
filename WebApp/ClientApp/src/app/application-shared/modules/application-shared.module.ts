import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { PrimengSharedModules } from './primeng-shared.module';
import { SharedComponentsModule } from './shared-components.module';
import { SharedPipesModule } from './shared-pipes.module';

@NgModule({
  exports: [
    PrimengSharedModules,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    SharedPipesModule,
    SharedComponentsModule,
  ],
})
export class ApplicationSharedModules {}
