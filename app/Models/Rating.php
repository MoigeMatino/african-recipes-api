<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Rating extends Model
{
    use HasFactory;

    protected $fillable = [
        'recipe_id',
        'user_id',
        'rating',
    ];

    // public function user(): BelongsToMany //Todo: Confirm this is needed
    // {
    //     return $this->belongsToMany(User::class, 'ratings', 'recipe_id', 'user_id')->withTimestamps();
    // }

    public function recipes(): BelongsToMany // Recipes with a certain rating
    {
        return $this->belongsToMany(Recipe::class, 'ratings', 'user_id', 'recipe_id')->withTimestamps();
    }
}
