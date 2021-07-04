import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ImageListFilterPipe } from '../pipes/ImageListFilter/ImageListFilter.pipe';

@NgModule({
  imports: [CommonModule],
  declarations: [ImageListFilterPipe],
  exports: [ImageListFilterPipe],
})
export class SharedPipesModule {}
