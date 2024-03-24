<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Recipe;
use App\Models\Tag;

class RecipeTagAssignmentSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $recipes = Recipe::all();
        $tags = Tag::all();

        foreach ($recipes as $recipe) {
            foreach ($tags as $tag) {
                $recipe->tags()->attach($tag->id);
            }
        }
    }
}
